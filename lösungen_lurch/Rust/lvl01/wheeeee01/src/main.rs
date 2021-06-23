use std::io::Write;

fn main() {
    print!("Enter MAX: ");
    std::io::stdout().flush().expect("Nicht geflusht");
    let number = get_number();

    for i in 1..=number {
        println!("{}", "#".repeat(i));
    }
}

fn get_number() -> usize {
    let mut buffer = String::new();
    let stdin = std::io::stdin();

    stdin.read_line(&mut buffer).expect("BROKEN STDIN");

    let input = buffer.trim();

    input.parse().expect("Peng")
}
