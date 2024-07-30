import cromlech as cr

cr_input = "cargo_tracking\cromlech\ddd_cromlech.yaml"
cr_output = [[7, '100001P', '100002P', '100003P', '100004P', '100017N'], [0, 1, 2, 3, 5, 6, 8, '100000P', '100005P', '100006P', '100007P', '100008P', '100009P', '100010P', '100011P', '100012N', '100013P', '100014P', '100015P', '100016P', '100017P'], [4, '100000N', '100001N', '100002N', '100003N', '100004N', '100012P', '100013N', '100014N', '100015N', '100016N', '100017N']] 



cr.setup(cr_input)

result_only_nums = []
for m in cr_output:
    ops = [x for x in m if isinstance(x, int)]
    attrs = [x for x in m if isinstance(x, str)]
    attrs_num = [int(x[:len(x) - 1]) for x in attrs]
    result_only_nums.append(ops + attrs_num)

cr.elect_primary_replicas(result_only_nums)

cr.format_and_draw_final(cr_output, "cargo_tracking\service_cutter\chinese_whisper.html")