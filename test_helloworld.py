import helloworld

def test_string():
  assert helloworld.hello_world() == "Hello World"

def test_num():
  assert helloworld.numerical(1) == 2