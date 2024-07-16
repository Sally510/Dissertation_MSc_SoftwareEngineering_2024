import cromlech as cr
import json

cr_input = ".\cromlech\jpet_servicecutter_to_cromlech.yaml"
cr_output = [[8, 9, 10, 11, 12, '100018P', '100019P', '100020P', '100021P', '100022P', '100023P', '100024P', '100025P', '100026P', '100027P', '100028P', '100029P', '100030P', '100058P'], [0, 1, 2, 3, '100000P', '100001P', '100002P', '100003P', '100004P', '100005P', '100006P', '100007P', '100008P', '100009P', '100010P', '100011P', '100012P', '100013P', '100014P', '100015P', '100016P', '100017P'], [13, 14, 15, '100016R', '100019N', '100020N', '100021N', '100022R', '100023R', '100024R', '100025R', '100026R', '100027R', '100028R', '100029R', '100030R', '100031P', '100032P', '100033P', '100034P', '100035P', '100036P', '100037P', '100038P', '100039P', '100040P', '100041P', '100042P', '100043P', '100044P', '100045P', '100046P', '100047P', '100048P', '100049P', '100050P', '100051P', '100052P', '100053P', '100054P', '100055P', '100056P', '100058R'], [4, 5, 6, 7, '100022R', '100023R', '100024R', '100025R', '100026R', '100027R', '100028R', '100029R', '100057P', '100058R']]

cr.setup(cr_input)

result_only_nums = []
for m in cr_output:
    ops = [x for x in m if isinstance(x, int)] 
    attrs = [x for x in m if isinstance(x, str)]
    attrs_num = [int(x[:len(x) - 1]) for x in attrs]
    result_only_nums.append(ops + attrs_num)
    
cr.elect_primary_replicas(result_only_nums)

cr.format_and_draw_final(cr_output, "jpet.html")

cr.output_to_microvalid(cr_output, "microvalid/microvalid_0.5.json") 

