use regex::Regex;
use std::env;
use std::fs;
use std::fs::File;
use std::io::{BufRead, BufReader, BufWriter, Write};
use std::path::Path;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("Filtering the text. Args: {:?}", args);
    let input_path = &args[1];
    let pattern = &args[2];
    let output_path = &args[3];

    let regex = Regex::new(pattern).unwrap();

    let output_dir = Path::new(output_path).parent().unwrap().to_str().unwrap();
    fs::create_dir_all(output_dir).unwrap();

    let input_file = File::open(input_path).unwrap();
    let output_file = File::create(output_path).unwrap();
    let input_reader = BufReader::new(input_file);
    let mut output_writer = BufWriter::new(output_file);
    for line in input_reader.lines() {
        let line_str = line.unwrap();
        if regex.is_match(&line_str) {
            output_writer.write_all(line_str.as_bytes()).unwrap();
        }
    }
}
