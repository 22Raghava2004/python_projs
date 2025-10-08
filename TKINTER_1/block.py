import tkinter as tk
import hashlib

# ------------------------------
# Blockchain Logic
# ------------------------------

# Function to calculate hash
def calculate_hash(index, data, nonce, prev_hash):
    block_contents = f"{index}{data}{nonce}{prev_hash}"
    return hashlib.sha256(block_contents.encode()).hexdigest()

# Proof-of-work mining (simple: hash must start with '000')
def mine_block(index, data, prev_hash):
    nonce = 0
    while True:
        hash_val = calculate_hash(index, data, nonce, prev_hash)
        if hash_val.startswith("000"):
            return nonce, hash_val
        nonce += 1

# Generate 5 blocks
def generate_blockchain():
    blockchain = []

    # Genesis block
    index = 0
    data = "Genesis Block"
    prev_hash = "0"
    nonce, hash_val = mine_block(index, data, prev_hash)
    blockchain.append({
        'index': index,
        'data': data,
        'nonce': nonce,
        'hash': hash_val,
        'prev_hash': prev_hash
    })

    # Next 4 blocks
    for i in range(1, 5):
        data = f"Block {i} Data"
        prev_hash = blockchain[i-1]['hash']
        nonce, hash_val = mine_block(i, data, prev_hash)
        blockchain.append({
            'index': i,
            'data': data,
            'nonce': nonce,
            'hash': hash_val,
            'prev_hash': prev_hash
        })

    return blockchain

# ------------------------------
# Tkinter GUI
# ------------------------------
def draw_blockchain(blockchain):
    root = tk.Tk()
    root.title("Graphical Blockchain Visualizer (5 Blocks with Security)")

    canvas_width = 1300
    canvas_height = 400
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    block_width = 200
    block_height = 180
    spacing = 50
    x = 30
    y = 100
    colors = ["#055c1b3a", "#0e731d", "#ffd5cc", "#598e14", "#6329bb"]

    for block in blockchain:
        index = block['index']
        data = block['data']
        nonce = block['nonce']
        hash_val = block['hash']
        prev_hash = block['prev_hash']

        # Draw rectangle for block
        canvas.create_rectangle(x, y, x + block_width, y + block_height,
                                fill=colors[index % len(colors)], outline='black', width=2)

        # Add block info
        canvas.create_text(x + 100, y + 20, text=f"Block #{index}", font=('Arial', 12, 'bold'))
        canvas.create_text(x + 100, y + 45, text=f"Data: {data}", font=('Arial', 10))
        canvas.create_text(x + 100, y + 70, text=f"Nonce: {nonce}", font=('Arial', 10))
        canvas.create_text(x + 100, y + 95, text=f"Hash:\n{hash_val[:20]}...", font=('Courier', 8))
        canvas.create_text(x + 100, y + 135, text=f"Prev Hash:\n{prev_hash[:20]}...", font=('Courier', 8))

        # Draw arrow to next block
        if index < len(blockchain) - 1:
            canvas.create_line(x + block_width, y + block_height / 2,
                               x + block_width + spacing, y + block_height / 2,
                               arrow=tk.LAST, width=2)
        x += block_width + spacing

    canvas.create_text(canvas_width / 2, 30,
                       text="Blockchain Visualization (Proof of Work - Hash starts with '000')",
                       font=('Arial', 14, 'bold'))

    root.mainloop()

# ------------------------------
# Run the Program
# ------------------------------
if __name__ == "__main__":
    blockchain = generate_blockchain()
    draw_blockchain(blockchain)
