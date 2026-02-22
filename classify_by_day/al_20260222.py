class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s: ## Email
            s = s.lower()
            s_split = s.split("@")
            if len(s_split[0]) >=2 :
                s_split[0] = f"{s_split[0][0]}*****{s_split[0][-1]}"
            return "@".join(s_split)

        else: ## Phone Number
            s = s.replace("(", "").replace(")", "").replace("-", "").replace("+", "").replace(" ", "")
            total_length = len(s)
            if total_length %10 == 0:
                return f"***-***-{s[-4:]}"
            elif total_length %10 == 1:
                return f"+*-***-***-{s[-4:]}"
            elif total_length % 10 == 2:
                return f"+**-***-***-{s[-4:]}"
            elif total_length % 10 == 3:
                return f"+***-***-***-{s[-4:]}"