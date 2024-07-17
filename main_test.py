import mock
import builtins
import main

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q1(capfd, monkeypatch):
    input_output = {
        '4, 2016': '2020 2024 2028 2032 ',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q1()
        out, _ = capfd.readouterr()
        assert out == v

def test_q2(capfd, monkeypatch):
    input_output = {
        '-1, 6, 4, 5': 'Primo\nNão\nNão\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q2()
        out, _ = capfd.readouterr()
        assert out == v


 