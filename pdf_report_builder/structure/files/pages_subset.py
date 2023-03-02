from typing import Sequence

class SubsetChunk:
    def __init__(self, *args, **kwargs) -> None:
        if args is None or len(args) == 0:
            raise AttributeError('Недостаточно атрибутов')
        if len(args) > 2:
            raise AttributeError('Слишком много атрибутов')
        self._start = 0
        self._stop = 1
        self._max_page_num = kwargs['max_page_num'] \
            if 'max_page_num' in kwargs \
            else None
        if len(args) == 1:
            s = args[0]
            if type(s) == int:
                self.start = s
                self.stop = None
                return
            elif isinstance(s, Sequence):
                s2 = tuple(map(int, s))
                self.start = min(s2)
                self.stop = max(s2)
                return
            else:         
                raise TypeError('Номера страниц описываются целыми числами')
        args_int = tuple(map(int, args))
        self.start = min(args_int)
        self.stop = max(args_int)
        return
    
    @property
    def start(self):
        return self._start
    
    @property
    def stop(self):
        return self._stop
    
    @start.setter
    def start(self, value: int):
        if value <= 0:
            raise ValueError('В PDF не может быть отрицательных и нулевых страниц')
        if not self._max_page_num is None and value > self._max_page_num:
            raise ValueError('Номер страницы больше дозволенного')
        self._start = value
    
    @stop.setter
    def stop(self, value: int | None):
        if not value is None and (value <= 0 or value <= self.start):
            raise ValueError('Некорректный номер страницы')
        if (
            not self._max_page_num is None \
            and not value is None \
            and value > self._max_page_num
        ):
            raise ValueError('Номер страницы больше дозволенного')
        self._stop = value

    def __str__(self):
        if self.stop is None: return str(self.start)
        return f'{self.start}-{self.stop}'
    
    def __len__(self):
        if self.stop == None: return 1
        return self.stop - self.start + 1
    
    def __iter__(self):
        self.counter = -1
        return self
    
    def __next__(self):
        self.counter += 1
        stop_iteration = self.counter > 0 \
            if self.stop is None \
            else self.start + self.counter > self.stop
        if stop_iteration:
            raise StopIteration
        return self.start + self.counter - 1
    
    @property
    def range(self):
        if self.stop is None: return (self.start)
        return range(self.start, self.stop + 1)

class PagesSubset:
    def __init__(
            self,
            chunks: list[SubsetChunk] | None = None,
            max_page_num: int | None = None
        ):
        self.chunks = [] if chunks is None else chunks
        self.max_page_num = max_page_num
    
    def add_chunk(self, chunk: Sequence):
        kwargs = {"max_page_num": self.max_page_num} \
            if not self.max_page_num is None \
            else {}
        new_chunk = SubsetChunk(chunk[0], chunk[1], **kwargs)
        self.chunks.append(new_chunk)
    
    def __iter__(self):
        self.current_chunk_index = 0
        if len(self.chunks) > 0:
            self.current_iter = iter(self.chunks[0])
        return self
    
    def __next__(self):
        if len(self.chunks) == 0:
            raise StopIteration
        try:
            next_val = next(self.current_iter)
        except StopIteration:
            self.current_chunk_index += 1
            if self.current_chunk_index >= len(self.chunks):
                raise StopIteration
            self.current_iter = iter(self.chunks[self.current_chunk_index])
            next_val = next(self.current_iter)
        return next_val
    
    def __str__(self):
        if len(self.chunks) == 0: return ''
        chunk_strings = [str(chunk) for chunk in self.chunks]
        return ','.join(chunk_strings)
    
    @staticmethod
    def from_string(
            input_string: str,
            max_page_num: int | None = None
        ):
        chunk_strings = input_string.strip().split(',')
        chunks = []
        kwargs = {"max_page_num": max_page_num} \
            if not max_page_num is None \
            else {}
        for s in chunk_strings:
            if '-' in s:
                start, stop = map(int, s.split('-'))
                chunks.append(SubsetChunk(start, stop, **kwargs))
            else:
                chunks.append(SubsetChunk(int(s), **kwargs))
        return PagesSubset(chunks, max_page_num)
