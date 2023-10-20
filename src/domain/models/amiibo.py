from dataclasses import dataclass

@dataclass  
class AmiiboUsage:
    usage: str
    write: bool

@dataclass
class GameUsage:
    game_name: str
    game_id: list[str] 
    amiiboUsage: list[AmiiboUsage]

@dataclass
class Game:
    gameUsage: list[GameUsage]

@dataclass
class AmiiboRelease:
    au: str
    eu: str
    jp: str
    na: str

@dataclass
class AmiiboCharacter:
    character: str
    amiiboSeries: str
    gameSeries: str
    head: str
    image: str
    name: str
    release: AmiiboRelease
    tail: str
    type: str
    games3DS: list[Game]
    gamesSwitch: list[Game]
    gamesWiiU: list[Game]

@dataclass
class GameSeries:
    key: str
    name: str
