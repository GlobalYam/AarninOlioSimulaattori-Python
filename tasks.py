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
def coverage_report(ctx):
    ctx.run("coverage report -m", pty = False)
