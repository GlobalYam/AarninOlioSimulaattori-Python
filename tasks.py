from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python src/run_program.py", pty = False) #pty = True)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest", pty = False)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty = False)
    ctx.run("coverage report -m", pty = False)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty = False)

@task
def lint(ctx):
    ctx.run("pylint src", pty = False)
