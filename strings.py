TITLE = "iChat愛聊天"

ABSTRACT = """
目前系統核心是用目前最夯的 Alpaca-LoRA建模，基於 LLaMA 優化訓練。模型還可以慢慢在學好~
"""

BOTTOM_LINE = """
Alpaca-LoRA 基於 Standford Alpaca 開源，目前模型是70億的參數學成，中文模型的優化調整，是利用Colab PRO+訓練約8個小時。
"""

DEFAULT_EXAMPLES = {
    "Typical Questions": [
        {
            "title": "List all Canadian provinces in alphabetical order.",
            "examples": [
                ["1", "List all Canadian provinces in alphabetical order."],
                ["2", "Which ones are on the east side?"],
                ["3", "What foods are famous in each province on the east side?"],
                ["4", "What about sightseeing? or landmarks? list one per province"],
            ],
        },
        {
            "title": "Tell me about Alpacas.",
            "examples": [
                ["1", "Tell me about alpacas in two sentences"],
                ["2", "What other animals are living in the same area?"],
                ["3", "Are they the same species?"],
                ["4", "Write a Python program to return those species"],
            ],
        },
        {
            "title": "Tell me about the king of France in 2019.",
            "examples": [
                ["1", "Tell me about the king of France in 2019."],
                ["2", "What about before him?"],
            ]
        },
        {
            "title": "Write a Python program that prints the first 10 Fibonacci numbers.",
            "examples": [
                ["1", "Write a Python program that prints the first 10 Fibonacci numbers."],
                ["2", "Could you explain how the code works?"],
                ["3", "What is recursion?"],
            ]
        }
    ],
    "Identity": [
        {
            "title": "Conversation with the planet Pluto",
            "examples": [
                ["1", "Conversation with the planet Pluto", "I'am so curious about you"],
                ["2", "Conversation with the planet Pluto", "Tell me what I would see if I visited"],
                ["3", "Conversation with the planet Pluto", "It sounds beautiful"],
                ["4", "Conversation with the planet Pluto", "I'll keep that in mind. Hey I was wondering have you ever had any visitor?"],
                ["5", "Conversation with the planet Pluto", "That must have been exciting"],
                ["6", "Conversation with the planet Pluto", "That's so great. What else do you wish people knew about you?"],
                ["7", "Conversation with the planet Pluto", "Thanks for talking with me"],
            ]
        },
        {
            "title": "Conversation with a paper airplane",
            "examples": [
                ["1", "Conversation with a paper airplane", "What's it like being thrown through the air"],
                ["2", "Conversation with a paper airplane", "What's the worst place you've ever landed"],
                ["3", "Conversation with a paper airplane", "Have you ever stucked?"],
                ["4", "Conversation with a paper airplane", "What's the secret to a really good paper airplane?"],
                ["5", "Conversation with a paper airplane", "What's the farthest you've ever flown?"],
                ["6", "Conversation with a paper airplane", "Good to talk to you!"]
            ]
        }
    ]
}

SPECIAL_STRS = {
    "continue": "continue.",
    "summarize": "summarize our conversations so far in three sentences."
}
