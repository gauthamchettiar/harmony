# tap-wordpress-reviews

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [WordPress Reviews](https://wordpress.org/plugins/wordpress-seo/#reviews)
- Extracts the following resources:
  - Reviews
- Outputs the schema for each resource
- Incrementally pulls data based on the input state


### Step 1: Configure

Create a file called `wp_reviews_config.json` in your working directory, following [sample_config.json](sample_config.json). The required parameters are `plugins`, which should be a list of plugins and `number` the number of reviews to fetch.

### Step 2: Install and Run

Create a virtual Python environment for this tap. This tap has been tested with Python 3.7, 3.8 and 3.9 and might run on future versions without problems.
```
python -m venv singer-wp-reviews
singer-wp-reviews/bin/python -m pip install --upgrade pip
singer-wp-reviews/bin/pip install git+https://github.com/Yoast/singer-tap-wordpress-reviews.git
```

This tap can be tested by piping the data to a local JSON target. For example:

Create a virtual Python environment with `singer-json`
```
python -m venv singer-json
singer-json/bin/python -m pip install --upgrade pip
singer-json/bin/pip install target-json
```

Test the tap:

```
singer-wp-reviews/bin/tap-wordpress-reviews -c wp_plugin_reviews_config.json | singer-json/bin/target-json
```

Copyright &copy; 2021 Yoast