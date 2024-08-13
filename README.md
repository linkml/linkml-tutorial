# LinkML Tutorial 1: Introduction to LinkML

This is a repository that walks through the LinkML modeling language, helpful LinkML command line tools, and 
automatic schema documentation generation. The main branch of this repository has the resulting
structure of a LinkML project that follows the tutorial to its completion.  If you want to walk through
the tutorial step by step, or refer back to a section of the tutorial at a later time, you can 
check out the stepped branches as needed.

For example, if you wanted to see the schema and infrastructure as it looks before implementing enumerations, 
you could refer to the `step_5_validation` branch.

For reference, the available sections are:

### Section 1: Setting up a LinkML project from scratch 

![1-cookiecutter.jpg](tutorial_slides%2F1-cookiecutter.jpg)
![2-cookiecutter.jpg](tutorial_slides%2F2-cookiecutter.jpg)
![3-cookiecutter.jpg](tutorial_slides%2F3-cookiecutter.jpg)
![4-cookiecutter.jpg](tutorial_slides%2F4-cookiecutter.jpg)
![5-cookiecutter.jpg](tutorial_slides%2F5-cookiecutter.jpg)

- [step_0_basic_project_creation](https://github.com/linkml/linkml-tutorial/tree/step_0_basic_project_creation)


### Section 2: Developing a model, validating the model with test data
![1a-modeling.jpg](tutorial_slides%2F1a-modeling.jpg)
![1-modeling.jpg](tutorial_slides%2F1-modeling.jpg)

- [step_1_model_components](https://github.com/linkml/linkml-tutorial/tree/step_1_model_components)
- [step_2_classes_and_slots](https://github.com/linkml/linkml-tutorial/tree/step_2_classes_and_slots)
- [step_3_hierarchies](https://github.com/linkml/linkml-tutorial/tree/step_3_hierarchies)
- [step_4_mappings_and_uris](https://github.com/linkml/linkml-tutorial/tree/step_4_mappings_and_uris)
- [step_5_validation](https://github.com/linkml/linkml-tutorial/tree/step_5_validation)
- [step_6_enumerations](https://github.com/linkml/linkml-tutorial/tree/step_6_enumerations)



### Section 3: Checking the model for best practices (linting)
- [step_7_linting](https://github.com/linkml/linkml-tutorial/tree/step_7_linting)
![1-linting.jpg](tutorial_slides%2F1-linting.jpg)
![1-validation.jpg](tutorial_slides%2F1-validation.jpg)
![1a-modeling.jpg](tutorial_slides%2F1a-modeling.jpg)


### Section 4: Generating model documentation
![1-doc.jpg](tutorial_slides%2F1-doc.jpg)
![2-doc-details.jpg](tutorial_slides%2F2-doc-details.jpg)
![3-doc-varieties.jpg](tutorial_slides%2F3-doc-varieties.jpg)
![4-doc-reststop.jpg](tutorial_slides%2F4-doc-reststop.jpg)

- [step_8_documentation](https://github.com/linkml/linkml-tutorial/tree/step_8_documentation)

### Section 5: Schemasheets
![1-schemasheets.jpg](tutorial_slides%2F1-schemasheets.jpg)
![2-schemasheets.jpg](tutorial_slides%2F2-schemasheets.jpg)
![3-schemasheets.jpg](tutorial_slides%2F3-schemasheets.jpg)
![4-schemasheets.jpg](tutorial_slides%2F4-schemasheets.jpg)
![5-schemasheets.jpg](tutorial_slides%2F5-schemasheets.jpg)
![6-schemasheets.jpg](tutorial_slides%2F6-schemasheets.jpg)

- [step_9_schemasheets](https://github.com/linkml/linkml-tutorial/tree/schemasheets)


## Website

* [https://linkml.github.io/linkml-tutorial](https://linkml.github.io/linkml-tutorial)

## Repository Structure

* [src/data/examples/](src/data/examples/Person-001.yaml) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [linkml_tutorial](src/linkml_tutorial)
        * [schema](src/linkml_tutorial/schema) -- LinkML schema (edit this)
* [datamodel](src/linkml_tutorial/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

Use the `make` command to generate project artifacts:

- `make all`: make everything
- `make deploy`: deploys site

To validate, create a poetry virtual environment, install the dependencies of this tutorial, and then
run the tests and/or linkml-validate.

```bash
poetry install
poetry run linkml-validate -s src/linkml_tutorial/schema/linkml_tutorial.yaml src/data/examples/Person-001.yaml --target-class PersonCollection
poetry run linkml-validate -s src/linkml_tutorial/schema/linkml_tutorial.yaml src/data/examples/Animal-001.yaml --target-class AnimalCollection
```

```bash
make test
```

To generate documentation locally (requires mkdocs):

```bash
make testdoc
```
and navigate to `http://127.0.0.1:8000/linkml-tutorial/`

To convert the test data from YAML to JSON, run:

```bash
poetry run linkml-convert -s src/linkml_tutorial/schema/linkml_tutorial.yaml -t json src/data/examples/Animal-001.yaml --target-class AnimalCollection
poetry run linkml-convert -s src/linkml_tutorial/schema/linkml_tutorial.yaml -t json src/data/examples/Person-001.yaml --target-class PersonCollection
```

To convert the test data from YAML to RDF, run:

```bash
poetry run linkml-convert -s src/linkml_tutorial/schema/linkml_tutorial.yaml -t rdf src/data/examples/Animal-001.yaml --target-class AnimalCollection
poetry run linkml-convert -s src/linkml_tutorial/schema/linkml_tutorial.yaml -t rdf src/data/examples/Person-001.yaml --target-class PersonCollection
```

To compile changed schemasheets, run:

```
make compile-sheets
```

For more information, please consult the [online LinkML tutorial](https://linkml.io/linkml/intro/tutorial01.html)
A link to a video tutorial is coming soon!


## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
