for /l %%x in (1, 1, 10) do ( 
    py grasp.py -i .\instances\2-FullIns_3.col  > .\output-grasp\2-FullIns_3-%%x.txt
    py grasp.py -i .\instances\queen5_5.col     > .\output-grasp\queen5_5-%%x.txt
    py grasp.py -i .\instances\queen6_6.col     > .\output-grasp\queen6_6-%%x.txt
    py grasp.py -i .\instances\queen7_7.col     > .\output-grasp\queen7_7-%%x.txt
    py grasp.py -i .\instances\queen9_9.col     > .\output-grasp\queen9_9-%%x.txt
    py grasp.py -i .\instances\queen11_11.col   > .\output-grasp\queen11_11-%%x.txt
    py grasp.py -i .\instances\4-FullIns_3.col  > .\output-grasp\4-FullIns_3-%%x.txt
    py grasp.py -i .\instances\5-FullIns_3.col  > .\output-grasp\5-FullIns_3-%%x.txt
    py grasp.py -i .\instances\queen10_10.col   > .\output-grasp\queen10_10-%%x.txt
    py grasp.py -i .\instances\2-FullIns_4.col  > .\output-grasp\2-FullIns_4-%%x.txt
)