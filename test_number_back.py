import number_back as n

#def test_save():
#    assert n.save(10) is True
#    assert n.save('10') is False
#    assert n.save(3.14) is False
#
#def test_find_all():
#    assert len(n.find_all())==0
#    n.save(100)
#    assert(len(n.find_all()))==1
#

def test_delete():
    n.save(10)
    n.save(20)
    n.save(30)
    n.save(20)
    assert n.delete(20)==True
    assert len(n.find_all())==2