from .jexl import JEXL
from .extended_grammar import ExtendedGrammar
import random
import math


class JexlExtended(JEXL):
    def __init__(self, context=None):
        super().__init__(context=context)
        self._extended_grammar = ExtendedGrammar(self)

        """ String functions """

        super().add_function("string", ExtendedGrammar.to_string)
        super().add_function("$string", ExtendedGrammar.to_string)
        super().add_transform("toString", ExtendedGrammar.to_string)
        super().add_transform("string", ExtendedGrammar.to_string)
        super().add_function("length", ExtendedGrammar.length)
        super().add_function("$length", ExtendedGrammar.length)
        super().add_transform("length", ExtendedGrammar.length)
        super().add_function("count", ExtendedGrammar.length)
        super().add_function("$count", ExtendedGrammar.length)
        super().add_transform("count", ExtendedGrammar.length)
        super().add_function("size", ExtendedGrammar.length)
        super().add_function("$size", ExtendedGrammar.length)
        super().add_transform("size", ExtendedGrammar.length)
        super().add_function("substring", ExtendedGrammar.substring)
        super().add_function("$substring", ExtendedGrammar.substring)
        super().add_transform("substring", ExtendedGrammar.substring)
        super().add_function("substringBefore", ExtendedGrammar.substring_before)
        super().add_function("$substringBefore", ExtendedGrammar.substring_before)
        super().add_transform("substringBefore", ExtendedGrammar.substring_before)
        super().add_function("substringAfter", ExtendedGrammar.substring_after)
        super().add_function("$substringAfter", ExtendedGrammar.substring_after)
        super().add_transform("substringAfter", ExtendedGrammar.substring_after)
        super().add_function("uppercase", ExtendedGrammar.uppercase)
        super().add_function("$uppercase", ExtendedGrammar.uppercase)
        super().add_transform("uppercase", ExtendedGrammar.uppercase)
        super().add_function("upper", ExtendedGrammar.uppercase)
        super().add_function("$upper", ExtendedGrammar.uppercase)
        super().add_transform("upper", ExtendedGrammar.uppercase)
        super().add_function("lowercase", ExtendedGrammar.lowercase)
        super().add_function("$lowercase", ExtendedGrammar.lowercase)
        super().add_transform("lowercase", ExtendedGrammar.lowercase)
        super().add_function("lower", ExtendedGrammar.lowercase)
        super().add_function("$lower", ExtendedGrammar.lowercase)
        super().add_transform("lower", ExtendedGrammar.lowercase)
        super().add_function("camelCase", ExtendedGrammar.camel_case)
        super().add_function("$camelCase", ExtendedGrammar.camel_case)
        super().add_transform("camelCase", ExtendedGrammar.camel_case)
        super().add_transform("camelcase", ExtendedGrammar.camel_case)
        super().add_transform("toCamelCase", ExtendedGrammar.camel_case)
        super().add_function("pascalCase", ExtendedGrammar.pascal_case)
        super().add_function("$pascalCase", ExtendedGrammar.pascal_case)
        super().add_transform("pascalCase", ExtendedGrammar.pascal_case)
        super().add_transform("pascalcase", ExtendedGrammar.pascal_case)
        super().add_transform("toPascalCase", ExtendedGrammar.pascal_case)
        super().add_function("trim", ExtendedGrammar.trim)
        super().add_function("$trim", ExtendedGrammar.trim)
        super().add_transform("trim", ExtendedGrammar.trim)
        super().add_function("pad", ExtendedGrammar.pad)
        super().add_function("$pad", ExtendedGrammar.pad)
        super().add_transform("pad", ExtendedGrammar.pad)
        super().add_function("contains", ExtendedGrammar.contains)
        super().add_function("$contains", ExtendedGrammar.contains)
        super().add_transform("contains", ExtendedGrammar.contains)
        super().add_function("includes", ExtendedGrammar.contains)
        super().add_function("$includes", ExtendedGrammar.contains)
        super().add_transform("includes", ExtendedGrammar.contains)
        super().add_function("split", ExtendedGrammar.split)
        super().add_function("$split", ExtendedGrammar.split)
        super().add_transform("split", ExtendedGrammar.split)
        super().add_function("join", ExtendedGrammar.join)
        super().add_function("$join", ExtendedGrammar.join)
        super().add_transform("join", ExtendedGrammar.join)
        super().add_function("replace", ExtendedGrammar.replace)
        super().add_function("$replace", ExtendedGrammar.replace)
        super().add_transform("replace", ExtendedGrammar.replace)
        super().add_function("base64Encode", ExtendedGrammar.base64_encode)
        super().add_function("$base64Encode", ExtendedGrammar.base64_encode)
        super().add_transform("base64Encode", ExtendedGrammar.base64_encode)
        super().add_function("base64Decode", ExtendedGrammar.base64_decode)
        super().add_function("$base64Decode", ExtendedGrammar.base64_decode)
        super().add_transform("base64Decode", ExtendedGrammar.base64_decode)

        """ Number functions """

        super().add_function("number", ExtendedGrammar.to_number)
        super().add_function("$number", ExtendedGrammar.to_number)
        super().add_transform("number", ExtendedGrammar.to_number)
        super().add_transform("toNumber", ExtendedGrammar.to_number)
        super().add_function("parseFloat", ExtendedGrammar.to_number)
        super().add_function("$parseFloat", ExtendedGrammar.to_number)
        super().add_transform("float", ExtendedGrammar.to_number)
        super().add_transform("toFloat", ExtendedGrammar.to_number)
        super().add_function("parseInteger", ExtendedGrammar.to_int)
        super().add_function("parseInt", ExtendedGrammar.to_int)
        super().add_function("$parseInteger", ExtendedGrammar.to_int)
        super().add_transform("parseInteger", ExtendedGrammar.to_int)
        super().add_transform("parseInt", ExtendedGrammar.to_int)
        super().add_transform("toInt", ExtendedGrammar.to_int)
        super().add_transform("integer", ExtendedGrammar.to_int)
        super().add_function("abs", ExtendedGrammar.abs)
        super().add_function("$abs", ExtendedGrammar.abs)
        super().add_transform("abs", ExtendedGrammar.abs)
        super().add_function("floor", ExtendedGrammar.floor)
        super().add_function("$floor", ExtendedGrammar.floor)
        super().add_transform("floor", ExtendedGrammar.floor)
        super().add_function("ceil", ExtendedGrammar.ceil)
        super().add_function("$ceil", ExtendedGrammar.ceil)
        super().add_transform("ceil", ExtendedGrammar.ceil)
        super().add_function("round", ExtendedGrammar.round)
        super().add_function("$round", ExtendedGrammar.round)
        super().add_transform("round", ExtendedGrammar.round)
        super().add_function("power", ExtendedGrammar.power)
        super().add_function("$power", ExtendedGrammar.power)
        super().add_transform("power", ExtendedGrammar.power)
        super().add_function("sqrt", ExtendedGrammar.sqrt)
        super().add_function("$sqrt", ExtendedGrammar.sqrt)
        super().add_transform("sqrt", ExtendedGrammar.sqrt)
        super().add_function("random", ExtendedGrammar.random)
        super().add_function("$random", ExtendedGrammar.random)
        super().add_function("formatNumber", ExtendedGrammar.format_number)
        super().add_function("$formatNumber", ExtendedGrammar.format_number)
        super().add_transform("formatNumber", ExtendedGrammar.format_number)
        super().add_function("formatBase", ExtendedGrammar.format_base)
        super().add_function("$formatBase", ExtendedGrammar.format_base)
        super().add_transform("formatBase", ExtendedGrammar.format_base)
        super().add_function("formatInteger", ExtendedGrammar.format_integer)
        super().add_function("$formatInteger", ExtendedGrammar.format_integer)
        super().add_transform("formatInteger", ExtendedGrammar.format_integer)
        super().add_function("sum", ExtendedGrammar.sum)
        super().add_function("$sum", ExtendedGrammar.sum)
        super().add_transform("sum", ExtendedGrammar.sum)
        super().add_function("max", ExtendedGrammar.max)
        super().add_function("$max", ExtendedGrammar.max)
        super().add_transform("max", ExtendedGrammar.max)
        super().add_function("min", ExtendedGrammar.min)
        super().add_function("$min", ExtendedGrammar.min)
        super().add_transform("min", ExtendedGrammar.min)
        super().add_function("avg", ExtendedGrammar.avg)
        super().add_function("$avg", ExtendedGrammar.avg)
        super().add_function("average", ExtendedGrammar.avg)
        super().add_function("$average", ExtendedGrammar.avg)
        super().add_transform("avg", ExtendedGrammar.avg)
        super().add_transform("average", ExtendedGrammar.avg)

        """ Boolean functions """

        super().add_function("boolean", ExtendedGrammar.to_boolean)
        super().add_function("$boolean", ExtendedGrammar.to_boolean)
        super().add_transform("boolean", ExtendedGrammar.to_boolean)
        super().add_function("bool", ExtendedGrammar.to_boolean)
        super().add_function("$bool", ExtendedGrammar.to_boolean)
        super().add_transform("bool", ExtendedGrammar.to_boolean)
        super().add_transform("toBoolean", ExtendedGrammar.to_boolean)
        super().add_transform("toBool", ExtendedGrammar.to_boolean)
        super().add_function("not", ExtendedGrammar.not_)
        super().add_function("$not", ExtendedGrammar.not_)
        super().add_transform("not", ExtendedGrammar.not_)

        """ Array functions """

        super().add_function("append", ExtendedGrammar.array_append)
        super().add_function("$append", ExtendedGrammar.array_append)
        super().add_transform("append", ExtendedGrammar.array_append)
        super().add_function("concat", ExtendedGrammar.array_append)
        super().add_function("$concat", ExtendedGrammar.array_append)
        super().add_transform("concat", ExtendedGrammar.array_append)
        super().add_function("reverse", ExtendedGrammar.array_reverse)
        super().add_function("$reverse", ExtendedGrammar.array_reverse)
        super().add_transform("reverse", ExtendedGrammar.array_reverse)
        super().add_function("shuffle", ExtendedGrammar.array_shuffle)
        super().add_function("$shuffle", ExtendedGrammar.array_shuffle)
        super().add_transform("shuffle", ExtendedGrammar.array_shuffle)
        super().add_function("sort", ExtendedGrammar.array_sort)
        super().add_function("$sort", ExtendedGrammar.array_sort)
        super().add_transform("sort", ExtendedGrammar.array_sort)
        super().add_function("order", ExtendedGrammar.array_sort)
        super().add_function("$order", ExtendedGrammar.array_sort)
        super().add_transform("order", ExtendedGrammar.array_sort)
        super().add_function("distinct", ExtendedGrammar.array_distinct)
        super().add_function("$distinct", ExtendedGrammar.array_distinct)
        super().add_transform("distinct", ExtendedGrammar.array_distinct)
        super().add_function("toObject", ExtendedGrammar.array_to_object)
        super().add_function("$toObject", ExtendedGrammar.array_to_object)
        super().add_transform("toObject", ExtendedGrammar.array_to_object)
        super().add_function("fromEntries", ExtendedGrammar.array_to_object)
        super().add_function("$fromEntries", ExtendedGrammar.array_to_object)
        super().add_transform("fromEntries", ExtendedGrammar.array_to_object)
        super().add_function("mapField", ExtendedGrammar.array_mapfield)
        super().add_function("$mapField", ExtendedGrammar.array_mapfield)
        super().add_transform("mapField", ExtendedGrammar.array_mapfield)
        super().add_function("map", self._extended_grammar.array_map)
        super().add_function("$map", self._extended_grammar.array_map)
        super().add_transform("map", self._extended_grammar.array_map)
        super().add_function("any", self._extended_grammar.array_any)
        super().add_function("$any", self._extended_grammar.array_any)
        super().add_transform("any", self._extended_grammar.array_any)
        super().add_function("some", self._extended_grammar.array_any)
        super().add_function("$some", self._extended_grammar.array_any)
        super().add_transform("some", self._extended_grammar.array_any)
        super().add_function("all", self._extended_grammar.array_every)
        super().add_function("$all", self._extended_grammar.array_every)
        super().add_transform("all", self._extended_grammar.array_every)
        super().add_function("every", self._extended_grammar.array_every)
        super().add_function("$every", self._extended_grammar.array_every)
        super().add_transform("every", self._extended_grammar.array_every)
        super().add_function("filter", self._extended_grammar.array_filter)
        super().add_function("$filter", self._extended_grammar.array_filter)
        super().add_transform("filter", self._extended_grammar.array_filter)
        super().add_function("find", self._extended_grammar.array_find)
        super().add_function("$find", self._extended_grammar.array_find)
        super().add_transform("find", self._extended_grammar.array_find)
        super().add_function("reduce", self._extended_grammar.array_reduce)
        super().add_function("$reduce", self._extended_grammar.array_reduce)
        super().add_transform("reduce", self._extended_grammar.array_reduce)

        """ Object functions """

        super().add_function("keys", ExtendedGrammar.object_keys)
        super().add_function("$keys", ExtendedGrammar.object_keys)
        super().add_transform("keys", ExtendedGrammar.object_keys)
        super().add_function("values", ExtendedGrammar.object_values)
        super().add_function("$values", ExtendedGrammar.object_values)
        super().add_transform("values", ExtendedGrammar.object_values)
        super().add_function("entries", ExtendedGrammar.object_entries)
        super().add_function("$entries", ExtendedGrammar.object_entries)
        super().add_transform("entries", ExtendedGrammar.object_entries)
        super().add_function("merge", ExtendedGrammar.object_merge)
        super().add_function("$merge", ExtendedGrammar.object_merge)
        super().add_transform("merge", ExtendedGrammar.object_merge)

        """ Date functions """
        super().add_function("now", ExtendedGrammar.now)
        super().add_function("$now", ExtendedGrammar.now)
        super().add_function("millis", ExtendedGrammar.millis)
        super().add_function("$millis", ExtendedGrammar.millis)
        super().add_function("millisToDateTime", ExtendedGrammar.to_datetime)
        super().add_function("$millisToDateTime", ExtendedGrammar.to_datetime)
        super().add_transform("millisToDateTime", ExtendedGrammar.to_datetime)
        super().add_function("fromMillis", ExtendedGrammar.to_datetime)
        super().add_function("$fromMillis", ExtendedGrammar.to_datetime)
        super().add_transform("fromMillis", ExtendedGrammar.to_datetime)
        super().add_function("toDateTime", ExtendedGrammar.to_datetime)
        super().add_function("$toDateTime", ExtendedGrammar.to_datetime)
        super().add_transform("toDateTime", ExtendedGrammar.to_datetime)
        super().add_function("dateTimeString", ExtendedGrammar.to_datetime)
        super().add_function("dateTimeToMillis", ExtendedGrammar.to_millis)
        super().add_function("$dateTimeToMillis", ExtendedGrammar.to_millis)
        super().add_transform("dateTimeToMillis", ExtendedGrammar.to_millis)
        super().add_function("toMillis", ExtendedGrammar.to_millis)
        super().add_function("$toMillis", ExtendedGrammar.to_millis)
        super().add_transform("toMillis", ExtendedGrammar.to_millis)
        super().add_function("dateTimeAdd", ExtendedGrammar.datetime_add)
        super().add_function("$dateTimeAdd", ExtendedGrammar.datetime_add)
        super().add_transform("dateTimeAdd", ExtendedGrammar.datetime_add)

        """ Misc """

        super().add_function("eval", ExtendedGrammar.eval_)
        super().add_function("$eval", ExtendedGrammar.eval_)
        super().add_transform("eval", ExtendedGrammar.eval_)
        super().add_function("uuid", ExtendedGrammar.uuid)
        super().add_function("$uuid", ExtendedGrammar.uuid)
        super().add_function("uid", ExtendedGrammar.uuid)
