# VIBE
**V**ocal acoustic **I**nversion to **B**iomechanical **E**stimates

VIBE reconstructs the time-dependent control parameters of a biomechanical model of the zebra finch (Taeniopygia guttata) syrinx directly from recorded song, recovering the physiological instructions underlying vocal production:

- **α(t)** — air sac pressure
- **β(t)** — syringeal muscle tension

These parameters are the coupled inputs to a nonlinear oscillator model of the syrinx ([Perl et al. 2011](https://doi.org/10.1103/physreve.84.051909); [Amador et al. 2013](https://doi.org/10.1038/nature11967)).

## Installation

```bash
pip install git+https://github.com/laurenostrowski/VIBE.git
```

Or clone and install locally:

```bash
git clone https://github.com/laurenostrowski/VIBE.git
cd VIBE
pip install -e .
```

Dependencies: `numpy`, `scipy`, `torch`, `matplotlib`, `joblib`, `tqdm`. Pitch estimation in the example notebooks optionally uses [`noisereduce`](https://github.com/timsainb/noisereduce) and the segmentation step uses [`vocalization-segmentation`](https://github.com/timsainb/vocalization-segmentation).


## Usage

### Fit a song

```python
from vibe import song_to_parameters

alpha, beta, fit_result = song_to_parameters(
    waveform,        # 1D audio waveform
    fs_audio,        # sample rate (Hz)
    vmask,           # boolean voicing mask, one value per STFT frame
    hop_length,      # STFT hop (samples)
    win_length,      # STFT window (samples)
    n_fft,           # FFT size
    pitch_kwargs=pitch_kwargs,   # optional per-bird pitch settings
)
```

`alpha` and `beta` are per-frame trajectories over the whole song. At voiced frames they are fit to the waveform; at unvoiced frames α follows a duration-dependent silence trajectory and β is held fixed. `fit_result` also contains the model amplitude, the optimizer positions, and the amplitude-fit correlation.

### Resynthesize from parameters

```python
from vibe import synthesize_song

rec_wav = synthesize_song(alpha, beta, fs_audio, len(waveform))
```

## Example notebooks

The `examples/` directory contains notebooks demonstrating segmentation, fitting, and resynthesis on example songs from three birds.

## Citation

If you use VIBE, please cite:

> Ostrowski LM, Méndez JM, Tostado PM, Cooper BG, Gentner TQ. Automated inference of respiratory and syringeal movement trajectories from birdsong acoustics. [in preparation].

The underlying biomechanical model is described in:

> Perl YS, Arneodo EM, Amador A, Mindlin GB. Reconstruction of physiological instructions from zebra finch song. *Phys Rev E* 84, 051909 (2011).

> Amador A, Perl YS, Mindlin GB, Margoliash D. Elemental gesture dynamics are encoded by song premotor cortical neurons. *Nature* 495, 59–64 (2013).

## License

VIBE is released under the MIT License. See [LICENSE](LICENSE) for details.

Copyright (c) 2026 Lauren Ostrowski

