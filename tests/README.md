# MagiCircles Unit Tests

```shell
cd ..  # MagiCircles/, where pyproject.toml lives
uv sync --group test
cd tests
uv run python manage.py test
```

To run a single test:

```shell
uv run python manage.py test test.tests.IChoicesTestModelTestCase.test_notification_icon
uv run python manage.py test test.test_utils.UtilsTestCase.test_markSafeJoin
```
