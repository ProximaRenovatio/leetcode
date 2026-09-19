class Solution:
        def checkOverlap(
                self,
                        radius: int,
                                xCenter: int,
                                        yCenter: int,
                                                x1: int,
                                                        y1: int,
                                                                x2: int,
                                                                        y2: int
                                                                            ) -> bool:

                                                                                    # If the center is inside the rectangle
                                                                                            if self.isInternal(x1, y1, x2, y2, xCenter, yCenter):
                                                                                                        return True

                                                                                                                # Find the closest point of the rectangle to the circle center
                                                                                                                        x = max(x1, min(xCenter, x2))
                                                                                                                                y = max(y1, min(yCenter, y2))

                                                                                                                                        # Check if this point is inside the circle
                                                                                                                                                dx = x - xCenter
                                                                                                                                                        dy = y - yCenter

                                                                                                                                                                return dx * dx + dy * dy <= radius * radius

                                                                                                                                                                    def isInternal(self, x1, y1, x2, y2, px, py) -> bool:
                                                                                                                                                                            cond = [
                                                                                                                                                                                        px >= x1,
                                                                                                                                                                                                    px <= x2,
                                                                                                                                                                                                                py >= y1,
                                                                                                                                                                                                                            py <= y2
                                                                                                                                                                                                                                    ]

                                                                                                                                                                                                                                            return all(cond)