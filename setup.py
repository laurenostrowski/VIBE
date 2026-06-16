from setuptools import setup, find_packages

setup(
    name="vibe",
    version="0.1.0",
    description="Vocal acoustic Inversion to Biomechanical Estimates: "
                "recover biomechanical trajectories from birdsong",
    author="Lauren Ostrowski",
    license="MIT",
    packages=find_packages(),
    package_data={"vibe": ["a_b_sweep.pkl"]},
    include_package_data=True,
    install_requires=[
        "numpy", "scipy", "torch", "matplotlib", "joblib", "tqdm",
        'importlib_resources; python_version < "3.9"',
    ],
    python_requires=">=3.8",
)
