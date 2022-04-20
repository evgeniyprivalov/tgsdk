#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015-2022 Evgeniy Privalov, https://linkedin.com/in/evgeniyprivalov/

from typing import List

from tgsdk import PassportElementError


class PassportElementErrorTranslationFiles(PassportElementError):
	"""
	https://core.telegram.org/bots/api#passportelementerrortranslationfiles

	"""
	__slots__ = (
		"source", "type", "file_hashes", "message"
	)

	def __init__(
		self,
		source: str,
		type: str,
		file_hashes: List[str],
		message: str
	):
		self.source = source
		self.type = type
		self.file_hashes = file_hashes
		self.message = message
