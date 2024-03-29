#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015-2022 Evgeniy Privalov, https://linkedin.com/in/evgeniyprivalov/

from typing import (
	Optional,
	Any
)

from tgsdk import TelegramEntity
from .photosize import PhotoSize


class Sticker(TelegramEntity):
	"""
	https://core.telegram.org/bots/api#sticker

	"""
	__slots__ = ("file_id", "file_unique_id", "width", "height", "is_animated", "thumb", "emoji", "set_name", "mask_position", "file_size")

	def __init__(
		self,
		file_id: str,
		file_unique_id: str,
		width: int,
		height: int,
		is_animated: bool,
		thumb: Optional[PhotoSize] = None,
		emoji: Optional[str] = None,
		set_name: Optional[str] = None,
		mask_position: Optional[str] = None,
		file_size: Optional[int] = None,

		**_kwargs: Any
	):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.width = width
		self.height = height
		self.is_animated = is_animated
		self.thumb = thumb
		self.emoji = emoji
		self.set_name = set_name
		self.mask_position = mask_position
		self.file_size = file_size
