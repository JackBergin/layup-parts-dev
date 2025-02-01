# Layup Parts Software Engineer Take Home Test

This folder contains two Python programs - a 2D airplane simulator and a sequence calculator.

## Setup

### Ensure you have Python installed on your machine. 

### To set the environment up, we will use a virtual environment and then install the requirements.

```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip3 install -r requirements.txt
```


#### *** NOTE: If you need to set up the virtual environment package and assuming you are working with WSL or Linux, you can run the following command to install the requirements:

```
sudo apt install python3-venv
```

## Running the Airplane Simulator

#### Controls

- Left Arrow Key: Turn yaw counterclockwise
- Right Arrow Key: Turn yaw clockwise
- Up Arrow Key: Increase speed
- Down Arrow Key: Decrease speed
- Spacebar: Reset position & speed

To run the airplane simulator, do the following:

```
python3 question1.py
```

## Running the Sequence Calculator

For the sequence calculator, run:

```
python3 question2.py
```

It was decided to not use recursion because python has a default recursion limit of 1000. This was a problem for the sequence calculator because the sequence grows exponentially. So, an iterative approach was used instead.