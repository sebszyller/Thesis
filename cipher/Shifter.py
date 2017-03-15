class Shifter:
    def __init__(self, distance, class_set):
        self.distance = distance
        self.class_set = list(class_set)
        self.max_idx = len(class_set) - 1

    # FIXME: might be slow as hell
    def shift(self, list_):
        # Given the list of unique elements in self.class_set
        # find index of the element and shift it by self.distance
        def next_(elem):
            current_idx = self.class_set.index(elem)
            target_idx = current_idx + self.distance
            if target_idx > self.max_idx:
                return self.class_set[target_idx - (self.max_idx + 1)]
            else:
                return self.class_set[target_idx]

        return map(next_, list_)
