import argparse

import numpy as np


from awgn.awgn import awgn_channel

def main():
    parser = argparse.ArgumentParser(description="AWGN Simulator")
    parser.add_argument("--snr_db", type=str, default="1.5,2.0,2.5,3.0,3.5,4.0", help="Signal-to-Noise Ratio in dB")
    parser.add_argument("--num_bits", type=int, default=100, help="Number of bits to simulate")
    args = parser.parse_args()

    encoded_bits = np.random.randint(0, 2, args.num_bits)

    snr_db = [*map(float, (args.snr_db).split(","))]
    rx_signal = [awgn_channel(encoded_bits, each_snr) for each_snr in snr_db]

    print("Received signal:", rx_signal)
    print("Received signal shape:", [each.shape for each in rx_signal])
    print("Received signal type:", [type(each) for each in rx_signal])
    print("Received signal dtype:", [each.dtype for each in rx_signal])

def batch():
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=10)

    parser = argparse.ArgumentParser(description="AWGN Simulator")
    parser.add_argument("--snr_db", type=str, default="1.5,2.0,2.5,3.0,3.5,4.0", help="Signal-to-Noise Ratio in dB")
    parser.add_argument("--num_bits", type=int, default=100, help="Number of bits to simulate")
    args = parser.parse_args()

    encoded_bits = np.random.randint(0, 2, args.num_bits)

    snr_db = [*map(float, (args.snr_db).split(","))]
    rx_signal = [awgn_channel(encoded_bits, each_snr) for each_snr in snr_db]

    print(*encoded_bits)
    for each in rx_signal:
        print(*each)
