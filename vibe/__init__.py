"""VIBE: Vocal acoustic Inversion to Biomechanical Estimates.

Fits a biomechanical model of the zebra finch vocal organ to recorded song,
recovering air sac pressure (alpha) and syringeal tension (beta) trajectories.
"""

from .core import (
    get_pitch,
    estimate_amplitude,
    song_to_parameters,
    synthesize_song,
    fitter,
    BiomechanicalSongFitter,
    ZebraFinchVocalTract,
    SNILCBounds,
    snilc,
)

__version__ = "0.1.0"

__all__ = [
    "get_pitch",
    "estimate_amplitude",
    "song_to_parameters",
    "synthesize_song",
    "fitter",
    "BiomechanicalSongFitter",
    "ZebraFinchVocalTract",
    "SNILCBounds",
    "snilc",
]
