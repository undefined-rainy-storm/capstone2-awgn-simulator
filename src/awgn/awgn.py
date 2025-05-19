import numpy as np

def awgn_channel(bits, snr_db):
    bpsk_symbols = 1 - 2 * bits

    snr_linear = 10 ** (snr_db / 10)
    noise_std = np.sqrt(1 / (2 * snr_linear))

    noise = noise_std * np.random.randn(len(bpsk_symbols))
    rx_signal = bpsk_symbols + noise

    return rx_signal

if __name__ == "__main__":
    encoded_bits = np.random.randint(0, 2, 1000)  # 이미 인코딩된 비트    
    snr_db = 2
    rx_signal = awgn_channel(encoded_bits, snr_db)
    print("Received signal:", rx_signal)
    print("Received signal shape:", rx_signal.shape)
    print("Received signal type:", type(rx_signal))
    print("Received signal dtype:", rx_signal.dtype)
