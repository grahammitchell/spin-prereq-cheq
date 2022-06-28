# spin-prereq-cheq

I don't know if you've ever tried to modify a Spinnaker pipeline by hand, but I have.

The most common mistake I make is renaming some stages (`refId`) and then forgetting to also change those names in the stages that depend on them (`requisiteStageRefIds`).

This is a tiny utility that walks through the stages, collecting a list of all the valid `refId`s and then makes sure all of your `requisiteStageRefIds` match up.

Use it like

```
$ ./spin-prereq-cheq.py path/to/pipeline.json
Checking 'path/to/pipeline.json'...
    All good!
```

You can provide multiple files at a time if you want:

```
$ ./spin-prereq-cheq.py path/to/pipeline.json  pipeline-branch.json
Checking 'path/to/pipeline.json'...
    All good!
Checking 'pipeline-branch.json'...
    Stage with refId 'foo' has requisiteStageRefId 'bar', which is not found.
```

