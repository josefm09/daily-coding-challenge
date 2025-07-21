const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { exec } = require('child_process');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static('public'));

// Ensure uploads directory exists
if (!fs.existsSync('uploads')) {
    fs.mkdirSync('uploads');
}

app.post('/encrypt', upload.single('file'), (req, res) => {
    try {
        const inputPath = req.file.path;
        const outputPath = inputPath + '.encrypted';
        
        // Use cargo run to encrypt the file
        exec(`cargo run --manifest-path ../Cargo.toml -- encrypt "${inputPath}" "${outputPath}"`, (error) => {
            if (error) {
                console.error('Encryption error:', error);
                return res.status(500).json({ error: 'Encryption failed' });
            }
            
            res.download(outputPath, req.file.originalname + '.encrypted', () => {
                // Cleanup files after sending
                fs.unlinkSync(inputPath);
                fs.unlinkSync(outputPath);
            });
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.post('/decrypt', upload.single('file'), (req, res) => {
    try {
        const inputPath = req.file.path;
        const outputPath = inputPath + '.decrypted';
        const originalName = req.file.originalname.replace('.encrypted', '');
        
        // Use cargo run to decrypt the file
        exec(`cargo run --manifest-path ../Cargo.toml -- decrypt "${inputPath}" "${outputPath}"`, (error) => {
            if (error) {
                console.error('Decryption error:', error);
                return res.status(500).json({ error: 'Decryption failed' });
            }
            
            res.download(outputPath, originalName, () => {
                // Cleanup files after sending
                fs.unlinkSync(inputPath);
                fs.unlinkSync(outputPath);
            });
        });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});