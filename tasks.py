from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python src/run_program.py", pty = True) #pty = False)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest", pty = True)

@task
def coverage_report(ctx):
    ctx.run("coverage report -m", pty = True)
