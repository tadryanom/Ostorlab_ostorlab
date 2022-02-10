"""Version utility class to make easy to compare semantic version strings."""
import semver


class Version:
    """Version class that only accepts semantic and provides python comparison API."""

    def __init__(self, version: str) -> None:
        """Init version."""
        semver.parse(version)
        self._version = version

    def __repr__(self):
        """Version string representation."""
        return f'<Version {self._version}>'

    def __lt__(self, other):
        """Pythonic comparison API."""
        if isinstance(other, Version):
            return semver.compare(self._version, other._version) < 0
        else:
            raise ValueError()

    def __le__(self, other):
        """Pythonic comparison API."""
        if isinstance(other, Version):
            return semver.compare(self._version, other._version) <= 0
        else:
            raise ValueError()

    def __gt__(self, other):
        """Pythonic comparison API."""
        if isinstance(other, Version):
            return semver.compare(self._version, other._version) > 0
        else:
            raise ValueError()

    def __ge__(self, other):
        """Pythonic comparison API."""
        if isinstance(other, Version):
            return semver.compare(self._version, other._version) >= 0
        else:
            raise ValueError()

    def __eq__(self, other):
        """Pythonic comparison API."""
        if isinstance(other, Version):
            return self._version == other._version
        else:
            raise ValueError()
