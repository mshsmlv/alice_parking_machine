# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import Any, Dict

from aiohttp.web import View, json_response, Response

PRE_DATA = {'version': '1.0'}


class Analyser(View):
    async def post(self):
        data = await self.request.json()
        print('response', data)

        answer: Dict[str, Any] = deepcopy(PRE_DATA)

        answer['session'] = {
            'session_id': data['session']['session_id'],
            'message_id': data['session']['message_id'],
            'user_id': data['session']['user_id'],
        }

        answer['response'] = {
            "text": "Здравствуйте! Это мы, хороводоведы.",
            "tts": "Здравствуйте! Это мы, хоров+одо в+еды.",
            'end_session': False,
        }

        print('answer', answer)
        return json_response(answer)

    async def get(self):
        return Response(text="Hello pal!")
