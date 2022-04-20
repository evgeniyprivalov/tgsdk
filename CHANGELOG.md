# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- 

## [1.1.0] - 2022-04-18
### Added
- New Entities:
    - `SentWebAppMessage`
    - `WebAppData`
    - `WebAppInfo`
    - `MenuButton`
    - `MenuButtonCommands`
    - `MenuButtonDefault`
    - `MenuButtonWebApp`
    - `KeyboardButtonPollType`
    - `InlineQueryResult`
    - `PassportElementError`
    - `PassportElementErrorDataField`
    - `PassportElementErrorFile`
    - `PassportElementErrorFiles`
    - `PassportElementErrorFrontSide`
    - `PassportElementErrorReverseSide`
    - `PassportElementErrorSelfie`
    - `PassportElementErrorTranslationFile`
    - `PassportElementErrorTranslationFiles`
    - `PassportElementErrorUnspecified`
- Add methods to the `Bot` entity:
    - `set_chat_menu_button`
    - `get_chat_menu_button`
    - `answer_web_app_query`
    - `answer_inline_query`
### Changed
- Methods `send_invoice`, `answer_shipping_query`, `answer_pre_checkout_query` of the `Bot` entity
- Update signature of some entities
- Updates some tests
### Removed


## [1.0.22] - 2022-04-11
### Added
- Add new field `has_protected_content` to `Message` entity
### Changed
- Update method `de_list` of the `TelegramEntity` entity
- Updates some tests
### Removed


## [1.0.20] - 2021-06-26
### Added
- Add new method `get_chat_member_count` to `Bot` entity
- Add new method `ban_chat_member` to `Bot` entity
### Changed
- Update entity `ReplyKeyboardMarkup`. Add field `input_field_placeholder`
- Change method `get_chat_members_count` in `Bot` entity. URL to API
- Change method `kick_chat_member` in `Bot` entity. URL to API
- Tests depends on changes
### Removed


## [1.0.0] - 2021-03-01
### Added
### Changed
### Removed
