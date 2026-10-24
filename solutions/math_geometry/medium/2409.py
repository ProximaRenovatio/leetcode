
class Solution:
    def countDaysTogether(
                self,
                        arriveAlice: str,
                                leaveAlice: str,
                                        arriveBob: str,
                                                leaveBob: str
    ) -> int:

            days = [31, 28, 31, 30, 31, 30,
                            31, 31, 30, 31, 30, 31]

                                    def to_days(date: str) -> int:
                                                month = int(date[:2])
                                                            day = int(date[3:])
                                                                        return sum(days[:month - 1]) + day

                                                                                start = max(to_days(arriveAlice), to_days(arriveBob))
                                                                                        end = min(to_days(leaveAlice), to_days(leaveBob))

                                                                                                return max(0, end - start + 1)

                                                                                                class Solution:
                                                                                                    def countDaysTogether(
                                                                                                            self,
                                                                                                                    arriveAlice: str,
                                                                                                                            leaveAlice: str,
                                                                                                                                    arriveBob: str,
                                                                                                                                            leaveBob: str
                                                                                                                                                ) -> int:

                                                                                                                                                        days = [31, 28, 31, 30, 31, 30,
                                                                                                                                                                        31, 31, 30, 31, 30, 31]

                                                                                                                                                                                def to_days(date: str) -> int:
                                                                                                                                                                                            month = int(date[:2])
                                                                                                                                                                                                        day = int(date[3:])
                                                                                                                                                                                                                    return sum(days[:month - 1]) + day

                                                                                                                                                                                                                            start = max(to_days(arriveAlice), to_days(arriveBob))
                                                                                                                                                                                                                                    end = min(to_days(leaveAlice), to_days(leaveBob))

                                                                                                                                                                                                                                            return max(0, end - start + 1)
                                                                                                                                                                                                                                            
    )