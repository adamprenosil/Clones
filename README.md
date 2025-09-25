# Closure with Majority Term

Algorithms for generating clones above an algebra that has a majority term.

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/gonzigaran/clausura-M.git
cd clausura-M/
```

Create and activate a virtual environment:

```bash
virtualenv env
source env/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Now the package is ready to use.

## Usage

Before running any command, make sure you are in the repository’s root directory and the virtual environment is activated:

```bash
cd clausura-M/
source env/bin/activate
```

This package computes **coclones** from a given algebra known to have a majority term.  
To do so, you first need to generate the algebra and save it as a `.model` file.

An example is provided in [algebra_generator_example.py](https://github.com/gonzigaran/clausura-M/blob/main/algebra_generator_example.py), which shows how to generate and store an algebra.  
The script uses decorators to simplify function definitions instead of writing the full operation tables manually. To run the example:

```bash
python algebra_generator_example.py
```

This will create the file `Models/exampleAlgebra.model`, which contains the universe on the first line, followed by the table of each function.

Once the algebra is generated, you can compute the coclones by running:

```bash
python gen_coclones.py "Models/exampleAlgebra.model"
```

After execution, logs will be stored in:

```
logs/exampleAlgebra.model
```