class Solution:
    def corpFlightBookings(self, bookings, n: int):
        l = n + 1
        b = [0] * l
        s = [0]
        for i in bookings:
            b[i[0] - 1] += i[2]
            b[i[1]] -= i[2]
        for j in b:
            s.append(j + s[-1])
        return s[1:l]

