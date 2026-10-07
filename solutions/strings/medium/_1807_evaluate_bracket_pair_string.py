class Solution:
	def evaluate(self, s, knowledge):
		# Store the knowledge pairs in a hash map
		# so we can look up each key in O(1) average time.
		knowledge_map = {}

		for key, value in knowledge:
			knowledge_map[key] = value

		result = []
		i = 0

		while i < len(s):

			if s[i] == '(':
				# Find the closing parenthesis
				j = i

				while s[j] != ')':
					j += 1

					# Extract the key between '(' and ')'
					key = s[i + 1:j]

				# Use '?' if the key does not exist
				value = knowledge_map.get(key, "?")

				result.append(value)

				# Move past the closing parenthesis
				i = j + 1

			else:
			# Normal character
				result.append(s[i])
				i += 1

		return ''.join(result)