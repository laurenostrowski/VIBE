from setuptools import setup, find_packages

setup(
    name="vibe",
    version="0.1.0",
    description="Vibrational Inversion to Biomechanical Estimates: "
                "recover biomechanical vocal parameters from birdsong",
    author="Lauren Ostrowski",
    license="MIT",
    packages=find_packages(),
    package_data={"vibe": ["a_b_sweep.pkl"]},
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "torch",
        "matplotlib",
        "joblib",
        "tqdm",
    ],
    python_requires=">=3.8",
)
