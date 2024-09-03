#!/usr/bin/env python
import sys
from socialpost.crew import SocialpostCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        "topic" : "AI, ML and Generative AI"
    }
    SocialpostCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        SocialpostCrew().crew().train(n_iterations=int(sys.argv[1]))

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
