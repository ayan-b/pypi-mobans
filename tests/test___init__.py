import jinja2
import pytest

path = './templates'


def get_rendered_file():
    context = {
        'name': 'dummy-0.0.0'
    }
    filename = '__init__.py.jj2'
    rendered = jinja2.Environment(
        loader=jinja2.FileSystemLoader(path)
    ).get_template(filename).render(context)
    return rendered


def test_underscore_replacement():
    rendered = get_rendered_file()
    assert 'dummy_0.0.0' in rendered
    assert 'dummy-0.0.0' not in rendered
