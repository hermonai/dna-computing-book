# MiniDNA

MiniDNA is the book's small executable vocabulary for sequence algebra and toy computational models. It favors explicit assumptions over physical realism.

Implemented milestones:

- M0 DNA alphabet and validation
- M1 immutable strand representation
- M2 complement and reverse complement
- M3 an aligned toy hybridization score
- M4 exact cutting and ligation
- PyTorch one-hot/complement parity bridge

The reaction, splicing, regulation, and expression modules establish small interfaces for later chapters. None is a wet-lab simulator.

```bash
python3 -m pytest
python3 code/minidna/examples/quick_start.py
```

