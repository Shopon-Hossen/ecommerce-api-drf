import os
import sys
import django
from django.urls import get_resolver, URLPattern, URLResolver


# Set the DJANGO_SETTINGS_MODULE environment variable to project's settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "e_commerce.settings")
sys.path.append(".")

# Initialize Django
django.setup()


def list_all_urls():
    resolver = get_resolver()
    urls = []

    def extract_urls(urlpatterns, prefix=""):
        for pattern in urlpatterns:
            if isinstance(pattern, URLResolver):
                new_prefix = prefix + str(pattern.pattern)
                extract_urls(pattern.url_patterns, new_prefix)
            elif isinstance(pattern, URLPattern):
                full_pattern = prefix + str(pattern.pattern)
                # Exclude URLs starting with "admin/"
                if not full_pattern.startswith("admin/"):
                    urls.append(full_pattern)

    extract_urls(resolver.url_patterns)
    return urls


def main():
    urls = list_all_urls()
    for url in urls:
        print(url)


if __name__ == "__main__":
    main()
