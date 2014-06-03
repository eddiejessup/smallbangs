Title: Saving a git commit hash to keep track of what code made what data
Date: 2013-05-12
Category: Programming
Tags: Python, Git

I have a sizeable chunk of python code that I use to run some simulations, that produce various bits of data that I dump into a directory. Since the code is reasonably complicated and I'm constantly fiddling with it, it seemed worth having a way to keep track of the state of the code alongside the output data, so if I find a bug I can see which results might have been affected by it.

I use git for version control, so to this end I've ended up storing the git hash of the latest commit alongisde the actual output data, and since it seems like a reasonably common situation here's how I do it (other methods are both available and probably better):

To get the hash of the latest commit you can use the [subprocess module](https://docs.python.org/2/library/subprocess.html) to grab it via a git command (there's probably several ways to get the hash but using rev-parse works),

```python
git_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip()
```

`check_output` takes a list of strings that it runs together as a command; the `strip()` removes a nasty little gremlin of a newline character that hitches a ride back from command land and the `--short` flag truncates the hash while maintaining uniqueness.

For the output bit, you could just dump it to a text file, but since you might end up wanting the parse it later on, why not get some structure in there to make it easier. To dump it to a [YAML](http://www.yaml.org) file (other data serialisation file formats are both available and probably worse), you'll be wanting a [yaml module](http://pyyaml.org/wiki/PyYAML) (pip install pyyaml or however you choose to source your pythons), then you can build a dictionary with the bits of information you want to dump,

```python
yaml_args = {}
yaml_args['git_hash'] = git_hash
# ...put in any other information about the run you want to keep, e.g. start time, parameters etc.
# yaml_args[...] = ...
# Dump the dictionary, formatted as YAML, to out.yaml in the directory dat_dir
yaml.dump(yaml_args, open('%s/out.yaml' % dat_dir, 'w'))
```

If you want to inspect the fields later on you can use yaml.safe_load(filename) to get back your python dictionary.
