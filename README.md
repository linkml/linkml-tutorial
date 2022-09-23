# linkml-tutorial-schema

A repostitory that walks through schema generation. 

## Website

* [https://linkml.github.io/linkml-tutorial-schema](https://linkml.github.io/linkml-tutorial-schema)

## Repository Structure

* [src/data/examples/](src/data/examples/Person-001.yaml) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [linkml_tutorial_schema](src/linkml_tutorial_schema)
        * [schema](src/linkml_tutorial_schema/schema) -- LinkML schema (edit this)
* [datamodel](src/linkml_tutorial_schema/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

Use the `make` command to generate project artifacts:

- `make all`: make everything
- `make deploy`: deploys site

To validate, create a poetry virtual environment, install the dependencies of this tutorial, and then
run the tests and/or linkml-validate.

```bash
poetry install
poetry run linkml-validate -s src/linkml_tutorial_schema/schema/linkml_tutorial_schema.yaml src/data/examples/Person-001.yaml --target-class PersonCollection
poetry run linkml-validate -s src/linkml_tutorial_schema/schema/linkml_tutorial_schema.yaml src/data/examples/Animal-001.yaml --target-class AnimalCollection
```

```bash
make test
```


## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
