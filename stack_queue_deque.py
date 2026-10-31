"""Stack, Queue və Deque – konsol mini tətbiqi.

İşə salmaq üçün:  python stack_queue_deque.py
"""
from collections import deque

MAX = 8


class DolduError(Exception):
    pass


class BosdurError(Exception):
    pass


class Struktur:
    """Üç strukturun ümumi bazası (daxildə collections.deque istifadə olunur)."""

    def __init__(self, max_olcu=MAX):
        self._data = deque()
        self.max_olcu = max_olcu

    def _yoxla_dolu(self):
        if len(self._data) >= self.max_olcu:
            raise DolduError(f"Struktur doludur (maksimum {self.max_olcu} element).")

    def _yoxla_bos(self):
        if not self._data:
            raise BosdurError("Struktur boşdur, çıxarılacaq element yoxdur.")

    def bosdur(self):
        return not self._data

    def __len__(self):
        return len(self._data)

    def temizle(self):
        self._data.clear()


class Stack(Struktur):
    """LIFO: sonuncu girən birinci çıxır."""

    def push(self, x):
        self._yoxla_dolu()
        self._data.append(x)

    def pop(self):
        self._yoxla_bos()
        return self._data.pop()

    def peek(self):
        self._yoxla_bos()
        return self._data[-1]

    def goster(self):
        if self.bosdur():
            return "  (boşdur)"
        sətirlər = []
        for i, x in enumerate(reversed(self._data)):
            ok = "  <- üst" if i == 0 else ""
            sətirlər.append(f"  | {str(x):^5} |{ok}")
        sətirlər.append("  +-------+")
        return "\n".join(sətirlər)


class Queue(Struktur):
    """FIFO: birinci girən birinci çıxır."""

    def enqueue(self, x):
        self._yoxla_dolu()
        self._data.append(x)

    def dequeue(self):
        self._yoxla_bos()
        return self._data.popleft()

    def peek(self):
        self._yoxla_bos()
        return self._data[0]

    def goster(self):
        if self.bosdur():
            return "  (boşdur)"
        return "  ön -> " + " ".join(f"[{x}]" for x in self._data) + " <- arxa"


class Deque(Struktur):
    """Hər iki ucdan əlavə və silmə."""

    def add_first(self, x):
        self._yoxla_dolu()
        self._data.appendleft(x)

    def add_last(self, x):
        self._yoxla_dolu()
        self._data.append(x)

    def remove_first(self):
        self._yoxla_bos()
        return self._data.popleft()

    def remove_last(self):
        self._yoxla_bos()
        return self._data.pop()

    def goster(self):
        if self.bosdur():
            return "  (boşdur)"
        return "  ön <-> " + " ".join(f"[{x}]" for x in self._data) + " <-> arxa"


# ---------- Mini tətbiqlər ----------

def metereme_yoxla(s):
    """Stack ilə mötərizə yoxlayıcı."""
    st = []
    cut = {")": "(", "]": "[", "}": "{"}
    for i, ch in enumerate(s, 1):
        if ch in "([{":
            st.append(ch)
        elif ch in ")]}":
            if not st or st.pop() != cut[ch]:
                return f"Səhv: {i}-ci simvolda “{ch}” üçün uyğun açılış yoxdur."
    if st:
        return f"Səhv: {len(st)} mötərizə bağlanmayıb."
    return "İfadə düzgündür: bütün mötərizələr cütləşdi."


def palindrom_yoxla(s):
    """Deque ilə palindrom yoxlayıcı."""
    dq = deque(c.lower() for c in s if c.isalnum())
    if not dq:
        return "Hərf və ya rəqəm daxil et."
    addim = 0
    while len(dq) > 1:
        a, b = dq.popleft(), dq.pop()
        addim += 1
        if a != b:
            return f"Palindrom deyil: “{a}” ≠ “{b}” ({addim}-ci addım)."
    return f"Palindromdur ({addim} müqayisə)."


def cap_et(q):
    """Queue ilə çap növbəsi: növbəti sənədi çap edir."""
    return f"“{q.dequeue()}” çap olundu. Qalan: {len(q)}."


# ---------- Konsol interfeysi ----------

class Sayqac:
    n = 0

    @classmethod
    def novbeti(cls):
        cls.n += 1
        return str(cls.n)


def deyer_al():
    v = input("  Dəyər (boş buraxsan avtomatik): ").strip()
    return v or Sayqac.novbeti()


MENYULAR = {
    "stack": {
        "ad": "Stack (LIFO)",
        "emr": {
            "1": ("push", lambda s: s.push(deyer_al())),
            "2": ("pop", lambda s: print(f"  Çıxarıldı: {s.pop()}")),
            "3": ("peek", lambda s: print(f"  Üstdəki: {s.peek()}")),
            "4": ("Mötərizə yoxlayıcı", lambda s: print("  " + metereme_yoxla(input("  İfadə: ")))),
        },
    },
    "queue": {
        "ad": "Queue (FIFO)",
        "emr": {
            "1": ("enqueue", lambda q: q.enqueue(deyer_al())),
            "2": ("dequeue", lambda q: print(f"  Çıxarıldı: {q.dequeue()}")),
            "3": ("peek", lambda q: print(f"  Öndəki: {q.peek()}")),
            "4": ("Çap növbəsi: növbəti sənədi çap et", lambda q: print("  " + cap_et(q))),
        },
    },
    "deque": {
        "ad": "Deque",
        "emr": {
            "1": ("add_first", lambda d: d.add_first(deyer_al())),
            "2": ("add_last", lambda d: d.add_last(deyer_al())),
            "3": ("remove_first", lambda d: print(f"  Çıxarıldı: {d.remove_first()}")),
            "4": ("remove_last", lambda d: print(f"  Çıxarıldı: {d.remove_last()}")),
            "5": ("Palindrom yoxlayıcı", lambda d: print("  " + palindrom_yoxla(input("  Söz/ifadə: ")))),
        },
    },
}


def alt_menyu(acar, obyekt):
    m = MENYULAR[acar]
    while True:
        print(f"\n=== {m['ad']} ===")
        print(obyekt.goster())
        for k, (ad, _) in m["emr"].items():
            print(f"  {k}) {ad}")
        print("  t) Təmizlə    0) Geri")
        sec = input("Seçim: ").strip().lower()
        if sec == "0":
            return
        if sec == "t":
            obyekt.temizle()
            continue
        if sec not in m["emr"]:
            print("  Yanlış seçim.")
            continue
        try:
            m["emr"][sec][1](obyekt)
        except (DolduError, BosdurError) as e:
            print(f"  ! {e}")


def main():
    strukturlar = {"1": ("stack", Stack()), "2": ("queue", Queue()), "3": ("deque", Deque())}
    while True:
        print("\n===== Stack · Queue · Deque =====")
        print("  1) Stack\n  2) Queue\n  3) Deque\n  0) Çıxış")
        sec = input("Seçim: ").strip()
        if sec == "0":
            print("Sağ ol!")
            return
        if sec in strukturlar:
            acar, obyekt = strukturlar[sec]
            alt_menyu(acar, obyekt)
        else:
            print("  Yanlış seçim.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nSağ ol!")
