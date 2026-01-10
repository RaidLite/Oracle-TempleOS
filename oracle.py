import time
import sys

_seed = int(time.time_ns()) & 0xffffffff

def templeos_random():
    global _seed
    t = time.time_ns() & 0xffffffff
    _seed = (_seed ^ t) * 1103515245 + 12345
    _seed &= 0xffffffff
    return _seed

def templeos_random_float():
    return templeos_random() / 0xffffffff

def templeos_choice(seq):
    return seq[templeos_random() % len(seq)]

class God:
    def __init__(self, path, amount):
        self.words = self._read_words(path)
        self.amount = amount

    @staticmethod
    def _read_words(path):
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def _format_text(self, text):
        words = text.split()
        result = []

        for word in words:
            if templeos_random_float() > 0.3:
                word = word.capitalize()
            if templeos_random_float() < 0.05:
                word = word + '.'
            result.append(word)

        formatted = ' '.join(result)
        lines = []
        current = []
        length = 0

        for word in formatted.split():
            if length + len(word) + 1 > 60:
                lines.append(' '.join(current))
                current = [word]
                length = len(word)
            else:
                current.append(word)
                length += len(word) + 1

        if current:
            lines.append(' '.join(current))

        return '\n'.join(lines)

    def speak(self):
        selected = [templeos_choice(self.words) for _ in range(self.amount)]
        raw = ' '.join(selected)
        return self._format_text(raw)

def main():
    print("God says.... " + God("HAPPY.TXT", 32).speak())

if __name__ == "__main__":
    main()
