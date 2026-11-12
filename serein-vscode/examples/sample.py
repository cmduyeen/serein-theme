"""A valid Python sample for syntax and Vietnamese glyph inspection."""
from dataclasses import dataclass


@dataclass
class ReadingSession:
    name: str
    minutes: int = 25

    def describe(self) -> str:
        # Comments remain upright and readable.
        if self.minutes <= 0:
            raise ValueError("Thời lượng phải lớn hơn 0")
        return f"{self.name}: {self.minutes} phút — nhớ nghỉ nhìn gần."


if __name__ == "__main__":
    print(ReadingSession("Nguyễn").describe())
