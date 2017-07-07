package #{package}.service.impl;

import java.util.List;

import #{package}.mapper.#{object}Mapper;
import #{package}.pojo.#{object};
import #{package}.service.I#{object}Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;

@Service
public class #{object}Service implements I#{object}Service{
	
	@Autowired
	private #{object}Mapper #{object_lower}Mapper;
	
	@Override
	public int save(#{object} record) {
		return #{object_lower}Mapper.insert(record);
	}

	@Override
	public int remove(#{object} record) {
		return #{object_lower}Mapper.delete(record);
	}

	@Override
	public int updateByPrimaryKey(#{object} record) {
		return #{object_lower}Mapper.updateByPrimaryKey(record);
	}

	@Override
	public int countAllRecord() {
		return #{object_lower}Mapper.countByExample(null);
	}

	@Override
	public #{object} getByPrimaryKey(Object key) {
		return #{object_lower}Mapper.selectByPrimaryKey(key);
	}

	@Override
	public List<#{object}> listAll() {
		return #{object_lower}Mapper.selectAll();
	}

	@Override
	public List<#{object}> listByPage(Page<#{object}> page) {
		PageHelper.startPage(page.getPageNum(), page.getPageSize(), page.isCount());
		return #{object_lower}Mapper.selectAll();
	}
	
}
