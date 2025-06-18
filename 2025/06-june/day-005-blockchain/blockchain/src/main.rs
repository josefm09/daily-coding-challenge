use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use chrono::Utc;
use log::info;
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use std::sync::Mutex;

#[derive(Debug, Clone, Serialize, Deserialize)]
struct Block {
    index: u64,
    timestamp: i64,
    data: String,
    previous_hash: String,
    hash: String,
    nonce: u64,
}

impl Block {
    fn new(index: u64, data: String, previous_hash: String) -> Self {
        let mut block = Block {
            index,
            timestamp: Utc::now().timestamp(),
            data,
            previous_hash,
            hash: String::new(),
            nonce: 0,
        };
        block.mine();
        block
    }

    fn calculate_hash(&self) -> String {
        let content = format!("{}{}{}{}{}",
            self.index,
            self.timestamp,
            self.data,
            self.previous_hash,
            self.nonce
        );
        let mut hasher = Sha256::new();
        hasher.update(content.as_bytes());
        format!("{:x}", hasher.finalize())
    }

    fn mine(&mut self) {
        let difficulty = 4; // Number of leading zeros required
        let target = "0".repeat(difficulty);

        while {
            self.hash = self.calculate_hash();
            !self.hash.starts_with(&target)
        } {
            self.nonce += 1;
        }

        info!("Block mined! Hash: {}", self.hash);
    }
}

#[derive(Debug, Clone, Serialize)]
struct Blockchain {
    chain: Vec<Block>,
}

impl Blockchain {
    fn new() -> Self {
        let mut chain = Vec::new();
        chain.push(Block::new(
            0,
            String::from("Genesis Block"),
            String::from("0"),
        ));
        Blockchain { chain }
    }

    fn add_block(&mut self, data: String) -> &Block {
        let previous_block = self.chain.last().unwrap();
        let new_block = Block::new(
            self.chain.len() as u64,
            data,
            previous_block.hash.clone(),
        );
        self.chain.push(new_block);
        self.chain.last().unwrap()
    }

    fn is_valid(&self) -> bool {
        for i in 1..self.chain.len() {
            let current_block = &self.chain[i];
            let previous_block = &self.chain[i - 1];

            if current_block.hash != current_block.calculate_hash() ||
               current_block.previous_hash != previous_block.hash {
                return false;
            }
        }
        true
    }
}

// Web server state
struct AppState {
    blockchain: Mutex<Blockchain>,
}

// API endpoints
async fn get_chain(data: web::Data<AppState>) -> impl Responder {
    let blockchain = data.blockchain.lock().unwrap();
    HttpResponse::Ok().json(&*blockchain)
}

#[derive(Deserialize)]
struct BlockData {
    data: String,
}

async fn mine_block(data: web::Json<BlockData>, app_state: web::Data<AppState>) -> impl Responder {
    let mut blockchain = app_state.blockchain.lock().unwrap();
    let block = blockchain.add_block(data.data.clone());
    HttpResponse::Ok().json(block)
}

async fn validate_chain(data: web::Data<AppState>) -> impl Responder {
    let blockchain = data.blockchain.lock().unwrap();
    let is_valid = blockchain.is_valid();
    HttpResponse::Ok().json(is_valid)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();
    
    let blockchain = web::Data::new(AppState {
        blockchain: Mutex::new(Blockchain::new()),
    });

    info!("Starting blockchain server at http://localhost:8080");

    HttpServer::new(move || {
        App::new()
            .app_data(blockchain.clone())
            .route("/chain", web::get().to(get_chain))
            .route("/mine", web::post().to(mine_block))
            .route("/validate", web::get().to(validate_chain))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
