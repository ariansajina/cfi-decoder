"""Data integrity tests for CFI lookup tables."""

from cfi_decoder._data import ATTRIBUTES, CATEGORIES, GROUPS


class TestCategories:
    def test_keys_are_single_uppercase_letters(self) -> None:
        for key in CATEGORIES:
            assert len(key) == 1
            assert key.isalpha()
            assert key.isupper()

    def test_values_are_non_empty_strings(self) -> None:
        for value in CATEGORIES.values():
            assert isinstance(value, str)
            assert len(value) > 0


class TestGroups:
    def test_every_category_has_groups(self) -> None:
        for cat in CATEGORIES:
            assert cat in GROUPS, f"Category {cat!r} has no groups defined"

    def test_keys_are_single_uppercase_letters(self) -> None:
        for cat, group_map in GROUPS.items():
            for key in group_map:
                assert len(key) == 1, f"Group key {key!r} in {cat!r}"
                assert key.isalpha(), f"Group key {key!r} in {cat!r}"
                assert key.isupper(), f"Group key {key!r} in {cat!r}"

    def test_values_are_non_empty_strings(self) -> None:
        for group_map in GROUPS.values():
            for value in group_map.values():
                assert isinstance(value, str)
                assert len(value) > 0


class TestAttributes:
    def test_every_group_has_attributes(self) -> None:
        for cat, group_map in GROUPS.items():
            for grp in group_map:
                assert (cat, grp) in ATTRIBUTES, f"No attributes for ({cat!r}, {grp!r})"

    def test_tuples_have_exactly_4_elements(self) -> None:
        for key, attrs in ATTRIBUTES.items():
            assert len(attrs) == 4, f"Attributes for {key} has {len(attrs)} elements"

    def test_each_element_is_label_dict_pair(self) -> None:
        for key, attrs in ATTRIBUTES.items():
            for i, attr in enumerate(attrs):
                assert isinstance(attr, tuple), (
                    f"Attribute {i} for {key} is not a tuple"
                )
                assert len(attr) == 2, (
                    f"Attribute {i} for {key} has {len(attr)} elements"
                )
                label, values = attr
                assert isinstance(label, str), (
                    f"Label for attribute {i} of {key} is not str"
                )
                assert len(label) > 0, f"Label for attribute {i} of {key} is empty"
                assert isinstance(values, dict), (
                    f"Values for attribute {i} of {key} is not dict"
                )

    def test_attribute_dicts_are_non_empty(self) -> None:
        for key, attrs in ATTRIBUTES.items():
            for i, (label, values) in enumerate(attrs):
                assert len(values) > 0, (
                    f"Empty values dict for attribute {i} ({label}) of {key}"
                )

    def test_attribute_dict_values_are_non_empty_strings(self) -> None:
        for key, attrs in ATTRIBUTES.items():
            for i, (label, values) in enumerate(attrs):
                for char, desc in values.items():
                    assert isinstance(desc, str), (
                        f"Value for {char!r} in attribute {i} ({label}) "
                        f"of {key} is not str"
                    )
                    assert len(desc) > 0, (
                        f"Empty description for {char!r} in attribute {i} "
                        f"({label}) of {key}"
                    )

    def test_attribute_dict_keys_are_single_uppercase_letters(self) -> None:
        for key, attrs in ATTRIBUTES.items():
            for i, (label, values) in enumerate(attrs):
                for char in values:
                    assert len(char) == 1, (
                        f"Key {char!r} in attribute {i} ({label}) of {key}"
                    )
                    assert char.isalpha() or char == "X", (
                        f"Key {char!r} in attribute {i} ({label}) of {key}"
                    )
                    assert char.isupper(), (
                        f"Key {char!r} in attribute {i} ({label}) of {key}"
                    )

    def test_no_extra_attribute_keys(self) -> None:
        """Every key in ATTRIBUTES corresponds to a valid (category, group) pair."""
        for cat, grp in ATTRIBUTES:
            assert cat in GROUPS, f"Category {cat!r} not in GROUPS"
            assert grp in GROUPS[cat], f"Group {grp!r} not in GROUPS[{cat!r}]"
