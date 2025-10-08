import tkinter as tk
import hashlib

# ------------------------------
# Blockchain Logic
# ------------------------------
def calculate_hash(index, data, nonce, prev_hash):
    """
    Calculates the SHA-256 hash for a block.
    The hash is based on the block's index, data, nonce, and previous hash.
    """
    block_contents = f"{index}{data}{nonce}{prev_hash}"
    return hashlib.sha256(block_contents.encode()).hexdigest()

def mine_block(index, data, prev_hash):
    """
    Mines a new block by finding a nonce that results in a hash
    starting with '000' (the proof-of-work difficulty).
    """
    nonce = 0
    # Keep incrementing the nonce until the hash meets the difficulty requirement
    while True:
        hash_val = calculate_hash(index, data, nonce, prev_hash)
        # Difficulty target: hash must start with "000"
        if hash_val.startswith("000"):
            return nonce, hash_val
        nonce += 1

def generate_blockchain(num_blocks=5):
    """
    Generates a chain of blocks, starting with the Genesis block.
    """
    blockchain = []
    
    # --- 1. Genesis Block ---
    index = 0
    data = "Genesis Block"
    prev_hash = "0"  # Convention for the first block's previous hash
    
    print(f"Mining Genesis Block ({index})...")
    nonce, hash_val = mine_block(index, data, prev_hash)
    
    blockchain.append({
        'index': index,
        'data': data,
        'nonce': nonce,
        'hash': hash_val,
        'prev_hash': prev_hash
    })
    print(f"Block {index} Mined. Hash: {hash_val}\n")

    # --- 2. Subsequent Blocks ---
    for i in range(1, num_blocks):
        data = f"Block {i} Data (Transaction Set {i})"
        # The previous hash is the hash of the last block in the chain
        prev_hash = blockchain[i-1]['hash']
        
        print(f"Mining Block {i}...")
        nonce, hash_val = mine_block(i, data, prev_hash)
        
        blockchain.append({
            'index': i,
            'data': data,
            'nonce': nonce,
            'hash': hash_val,
            'prev_hash': prev_hash
        })
        print(f"Block {i} Mined. Hash: {hash_val}\n")
        
    return blockchain

# ------------------------------
# Gradient colors for rectangles
# ------------------------------
def gradient_colors(num_blocks):
    """
    Provides a list of visually distinct colors for the blocks.
    """
    base_colors = [
        '#ff4d4d',  # Red
        '#ffb84d',  # Orange
        '#ffff4d',  # Yellow
        '#4dff88',  # Green
        '#4da6ff',  # Blue
        '#b84dff',  # Purple
        '#ff66cc',  # Pink
        '#66ffff',  # Cyan
    ]
    colors = []
    for i in range(num_blocks):
        # Cycle through the base colors
        colors.append(base_colors[i % len(base_colors)])
    return colors

# ------------------------------
# Tkinter GUI
# ------------------------------
def draw_blockchain(blockchain):
    """
    Uses Tkinter to draw the blockchain visualization.
    """
    rect_width = 250  # Increased width for better text spacing
    rect_height = 160 # Increased height
    spacing = 50      # Increased spacing between blocks
    
    # Calculate required canvas width
    canvas_width = len(blockchain) * rect_width + (len(blockchain) - 1) * spacing + 100
    canvas_height = 450

    root = tk.Tk()
    root.title("Proof-of-Work Blockchain Visualizer")
    root.geometry(f"{canvas_width}x{canvas_height}")
    root.resizable(False, False)

    # Use a dark, professional theme
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='#1e1e1e')
    canvas.pack(pady=20, padx=20)

    colors = gradient_colors(len(blockchain))

    x = 50  # Starting X position
    y = 120 # Starting Y position
    
    # Set text color inside blocks to white for high contrast, matching the image
    text_color = 'white' 

    for i, block in enumerate(blockchain):
        color = colors[i]
        
        # Draw shadow rectangle for depth
        canvas.create_rectangle(x + 5, y + 5, x + rect_width + 5, y + rect_height + 5, 
                                fill='#000000', outline='', tags=f"block_{i}")

        # Draw main rectangle for block
        canvas.create_rectangle(x, y, x + rect_width, y + rect_height, 
                                fill=color, outline='#ffffff', width=3, tags=f"block_{i}")

        # Block info inside rectangle (using white text for high contrast)
        center_x = x + rect_width / 2
        
        # Title
        canvas.create_text(center_x, y + 25, text=f"BLOCK #{block['index']}", 
                           font=('Roboto', 14, 'bold'), fill=text_color, tags=f"block_{i}")
        
        # Data
        canvas.create_text(center_x, y + 55, text=f"Data: {block['data']}", 
                           font=('Courier New', 10), fill=text_color, tags=f"block_{i}")
        
        # Nonce
        canvas.create_text(center_x, y + 80, text=f"Nonce: {block['nonce']}", 
                           font=('Courier New', 10), fill=text_color, tags=f"block_{i}")
        
        # Hash (First 20 chars)
        canvas.create_text(center_x, y + 105, text=f"Hash: {block['hash'][:20]}...", 
                           font=('Courier New', 8), fill=text_color, tags=f"block_{i}")
        
        # Prev Hash (First 20 chars)
        canvas.create_text(center_x, y + 130, text=f"Prev Hash: {block['prev_hash'][:20]}...", 
                           font=('Courier New', 8), fill=text_color, tags=f"block_{i}")

        # Arrow to next block
        if block['index'] < len(blockchain) - 1:
            arrow_start_x = x + rect_width
            arrow_end_x = x + rect_width + spacing
            arrow_y = y + rect_height / 2
            
            # Draw connecting arrow (chain)
            canvas.create_line(arrow_start_x, arrow_y,
                               arrow_end_x, arrow_y,
                               arrow=tk.LAST, width=4, fill='#66ccff', 
                               smooth=True, tags="chain_link")
            
            # Draw a small chain icon in the middle of the arrow
            mid_x = arrow_start_x + spacing / 2
            canvas.create_oval(mid_x - 7, arrow_y - 7, mid_x + 7, arrow_y + 7, 
                               fill="#89d2f6", outline='#ffffff', width=2, tags="chain_link")


        # Move x position for the next block
        x += rect_width + spacing

    # Heading at top - Reverting to a simpler structure to match the image better
    canvas.create_text(canvas_width / 2, 50, 
                       text="Blockchain Visualization (Hash starts with '000')",
                       font=('Roboto', 18, 'bold'), fill='#ffffff')
    
    # Removing the detailed subtitle to simplify the header area
    # canvas.create_text(canvas_width / 2, 80, 
    #                    text="Visualizing the cryptographic link via Prev Hash -> Hash",
    #                    font=('Roboto', 12), fill='#cccccc')


    root.mainloop()

# ------------------------------
# Run Program
# ------------------------------
if __name__ == "__main__":
    # Generate 5 blocks (including Genesis)
    blockchain = generate_blockchain(num_blocks=5) 
    
    # Visualize the generated chain
    draw_blockchain(blockchain)
